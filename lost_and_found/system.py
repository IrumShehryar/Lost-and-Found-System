def get_all_items(self) -> list:
    """
    Return a list of all items currently stored.

    :return: List of Item instances.
    """
    return self.items[:]  # Return a shallow copy to prevent external mutation