from shorty.Engines.BaseEngine import BaseEngine

class TestBaseEngine:
    
    def test_base_engine_name(self):
        engine = BaseEngine()
        assert engine.name == ""
