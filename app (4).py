from graph.research_graph import build_graph

def main():
    print("=== Multi-Agent Research Team ===")
    topic = input("Enter research topic: ").strip()

    if not topic:
        print("No topic provided. Exiting.")
        return

    graph = build_graph()

    print("\n[Running Research Pipeline...]\n")
    result = graph.invoke({"topic": topic})

    print("\n===== FINAL RESEARCH OUTPUT =====\n")
    print(result["final"])

if __name__ == "__main__":
    main()
