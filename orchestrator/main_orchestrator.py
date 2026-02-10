from pipelines import BugHuntingPipeline


def main():

    pipeline = BugHuntingPipeline(mcp_client=None)

    input_csv_path = "data/input/samples.csv"
    output_csv_path = "data/output/results.csv"

    pipeline.run(input_csv_path, output_csv_path)

    print("results.csv generated successfully.")


if __name__ == "__main__":
    main()
