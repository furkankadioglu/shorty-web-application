from shorty.Engines.BaseEngine import BaseEngine

class TestBaseEngine:
    
    def test_base_engine_api_endpoint(self):
        engine = BaseEngine()
        assert engine.name == ""
