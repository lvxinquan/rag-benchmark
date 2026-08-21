# rag-benchmark

An open-source benchmark toolkit for evaluating Retrieval-Augmented Generation systems.

![A transparent RAG evaluation pipeline from source documents through retrieval, generation, citations, and metrics](assets/hero.png)

> **Status: Foundation**
>
> No evaluation outputs have been published yet. This repository currently defines the project scope and engineering baseline.

## Motivation

RAG systems combine several independently fallible stages. A single end-to-end score can hide whether a failure came from ingestion, retrieval, ranking, context construction, generation, or citation behavior. `rag-benchmark` will focus on explicit evaluation boundaries and reproducible inputs.

## Planned Evaluation Layers

- **Retrieval:** hit rate, recall, ranking quality, and failure analysis
- **Context:** coverage, redundancy, and token-budget behavior
- **Generation:** groundedness, answer relevance, and abstention behavior
- **Citations:** source attribution and support verification
- **Systems:** latency and cost reporting with fully disclosed methodology

No metric implementation or benchmark result is claimed in the foundation release.

## Evaluation Principles

- Preserve dataset provenance and licensing information
- Separate retrieval metrics from answer-quality metrics
- Keep deterministic and model-judged evaluations distinguishable
- Version prompts, models, embeddings, and index configuration
- Publish raw outputs when publishing aggregate results
- Report limitations and known sources of variance

## Repository Structure

```text
rag-benchmark/
├── .github/workflows/  # Continuous integration
├── benchmarks/         # Versioned benchmark specifications
├── datasets/           # Dataset manifests and provenance
├── docs/               # Methodology and design notes
├── evaluators/         # Evaluator contracts and future implementations
├── examples/           # Tested usage examples
├── src/rag_benchmark/  # Python package
├── tests/              # Automated tests
└── pyproject.toml
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

CI covers Python 3.10, 3.11, and 3.12.

## Contributing

Early contributions should improve benchmark methodology, provenance requirements, evaluator contracts, or focused test infrastructure. New datasets must include their source, license, intended use, and limitations.

## License

Licensed under the [MIT License](LICENSE). Individual datasets may require separate licenses and notices.
