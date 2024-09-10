import csv
import json

def parse_plan(plan, parent_info=""):
    """
    Rekursive Funktion, um Plan Rows, Actual Rows und andere relevante Informationen
    wie Relation Name, Join Type, Scan Direction etc. aus einem verschachtelten Plan zu extrahieren.
    """
    estimated_rows = plan.get("Plan Rows", 0)
    actual_rows = plan.get("Actual Rows", 0)
    relation_name = plan.get("Relation Name", "XXX")
    node_type = plan.get("Node Type", "XXX")
    join_type = plan.get("Join Type", "XXX")
    scan_direction = plan.get("Scan Direction", "XXX")

    # Konstruiere zusätzliche Informationen
    additional_info = {
        "Relation Name": relation_name,
        "Node Type": node_type,
        "Join Type": join_type,
        "Scan Direction": scan_direction,
        "Parent Info": parent_info
    }

    # Initial check on the current level
    deviations = []
    if estimated_rows > 0:
        if estimated_rows != actual_rows:
            deviation1 = abs(actual_rows/estimated_rows)
            deviation = abs(1-deviation1) +1
            deviations.append((estimated_rows, actual_rows, deviation, additional_info))

    # Check for nested plans
    if "Plans" in plan:
        for subplan in plan["Plans"]:
            deviations.extend(parse_plan(subplan, node_type))

    return deviations

def identify_critical_misestimates(input_file, output_csv):
    critical_entries = []

    with open(input_file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            try:
                # Die Annahme ist, dass der JSON-Inhalt in der zweiten Spalte des CSV steht
                query_name = row[0]
                plan_json = json.loads(row[1])  # JSON-Inhalt parsen

                # Parsing the main plan
                plan = plan_json[0]["Plan"]
                deviations = parse_plan(plan)

                # Prüfen auf kritische Abweichungen
                for estimated_rows, actual_rows, deviation, additional_info in deviations:
                        critical_entries.append([
                            query_name,
                            estimated_rows,
                            actual_rows,
                            additional_info["Relation Name"],
                            additional_info["Node Type"],
                            additional_info["Join Type"],
                            additional_info["Scan Direction"],
                            additional_info["Parent Info"]
                        ])
            except (IndexError, ValueError, KeyError, json.JSONDecodeError) as e:
                print(f"Error processing row: {row}. Error: {e}")
                continue

    # Schreibe die kritischen Werte in eine neue CSV-Datei
    with open(output_csv, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            'Query Name',
            'Estimated Rows',
            'Actual Rows',
            'Relation Name',
            'Node Type',
            'Join Type',
            'Scan Direction',
            'Parent Node Type'
        ])  # Header

        for entry in critical_entries:
            csv_writer.writerow(entry)

    print(f"Critical misestimates have been identified and saved to {output_csv}")

# Aufruf der Funktion
input_file = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/explain_analysis_results.csv'
output_csv = '/Users/lui/PycharmProjects/BachelorProject_Ludwig_V2/IMDb/Resultfiles/CRITICAL_values_no_limit.csv'
identify_critical_misestimates(input_file, output_csv)


