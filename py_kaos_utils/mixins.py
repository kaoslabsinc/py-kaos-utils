# Credit to ChatGPT for this implementation
class TrackChangesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_values = {}

    def __setattr__(self, name, value):
        if name in self.Config.fields_to_track:
            # Save the original value of the field if it hasn't been saved yet
            if name not in self.__original_values:
                self.__original_values[name] = getattr(self, name)

        super().__setattr__(name, value)

    def has_field_changed(self, field_name):
        if field_name in self.__original_values:
            # Return whether the field's value has changed from the original value
            return getattr(self, field_name) != self.__original_values[field_name]
        else:
            # The field has not been changed if it doesn't have an original value
            return False


__all__ = (
    'TrackChangesMixin',
)
