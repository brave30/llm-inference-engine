def __getattr__(name):
    # lazy so that importing inference_engine.kernels doesn't pull in the whole engine
    if name == "LLMEngine":
        from inference_engine.engine import LLMEngine
        return LLMEngine
    if name == "SamplingParams":
        from inference_engine.sampling import SamplingParams
        return SamplingParams
    raise AttributeError(name)
