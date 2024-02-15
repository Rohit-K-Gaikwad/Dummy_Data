from typing import Dict, Any, List, Tuple

def get_train_with_lowest_fare(data: Dict[str, Any]) -> Tuple[str, str]:
    """
    Finds the train with the lowest fare across all classes and returns its name and code.

    Args:
        data: A dictionary containing information about trains.

    Returns:
        A tuple containing the train name and code with the lowest fare across all classes.
    """
    lowest_fare = float('inf')
    lowest_fare_train = None
    for train in data.get("trains", []):
        fare_info = train.get("fare", {})
        for class_type, class_fare_info in fare_info.items():
            gn_fare = class_fare_info.get("GN")
            if gn_fare is not None and gn_fare < lowest_fare:
                lowest_fare = gn_fare
                lowest_fare_train = (train.get("tname"), train.get("tcode"))
    return lowest_fare_train

# Example usage:
lowest_fare_train = get_train_with_lowest_fare(data)
if lowest_fare_train:
    print("Train with the lowest fare across all classes:")
    print("Train Name:", lowest_fare_train[0])
    print("Train Code:", lowest_fare_train[1])
else:
    print("No train found with fare information.")