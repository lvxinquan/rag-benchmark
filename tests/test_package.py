def test_package_exposes_version() -> None:
    from rag_benchmark import __version__

    assert __version__ == "0.1.0"

