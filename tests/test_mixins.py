import pytest
from unittest.mock import MagicMock


class TestTrackChangesMixin:
    @pytest.fixture
    def mock_model(self):
        """
        Fixture that returns a mock Model that uses the TrackChangesMixin
        """
        model = MagicMock()
        model.Config = MagicMock()
        model.Config.fields_to_track = ['name']
        model.name = "John"
        model.age = 30
        model.__original_values = {}
        model.__class__ = MagicMock()
        model.__class__.__name__ = 'MyModel'
        TrackChangesMixin.__init__(model)
        return model

    def test_has_field_changed(self, mock_model):
        assert not mock_model.has_field_changed("name")
        assert not mock_model.has_field_changed("age")

        mock_model.name = "Mark"
        assert mock_model.has_field_changed("name")
        assert not mock_model.has_field_changed("age")

    def test___setattr__(self, mock_model):
        # Test that original value is saved when field is in fields_to_track
        mock_model.name = "Mark"
        assert mock_model.__original_values == {'name': 'John'}

        # Test that original value is not saved when field is not in fields_to_track
        mock_model.age = 40
        assert mock_model.__original_values == {'name': 'John'}
