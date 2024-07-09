# Cars
def make_car(manufacturer, model_name, **features):
    """Build a dictionary containing features about a car."""
    features['manufacturer'] = manufacturer
    features['model_name'] = model_name
    return features


car = make_car('Porsche', '911', color='yellow', convertible=True)
print(car)