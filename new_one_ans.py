from typing import Dict, Any, List, Optional

def get_lowest_fare_across_classes(data: Dict[str, Any]) -> Dict[str, Optional[int]]:
    """
    Finds the lowest fare for each class across all train categories.

    Args:
        data: A dictionary containing information about trains.

    Returns:
        A dictionary containing the lowest fare for each class across all train categories.
    """
    lowest_fares = {}
    for train in data.get("trains", []):
        fare_info = train.get("fare", {})
        for class_type, class_fare_info in fare_info.items():
            gn_fare = class_fare_info.get("GN")
            if gn_fare is not None:
                current_lowest = lowest_fares.get(class_type)
                if current_lowest is None or gn_fare < current_lowest:
                    lowest_fares[class_type] = gn_fare
    return lowest_fares

# Example usage:
lowest_fares_across_classes = get_lowest_fare_across_classes(data)
for class_type, lowest_fare in lowest_fares_across_classes.items():
    if lowest_fare is not None:
        print(f"Lowest fare in {class_type} class: {lowest_fare}")
    else:
        print(f"No fare information available in {class_type} class.")