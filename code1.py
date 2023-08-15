import pandas as pd

# Load the star data into a Pandas DataFrame
stars = pd.read_csv('star_data.csv')

# Check for missing values and remove or impute them
stars.isna().sum() # Check for missing values
stars.dropna(inplace=True) # Remove rows with missing values

# Encode categorical variables using one-hot encoding
stars_encoded = pd.get_dummies(stars, columns=['spectral_class'])

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X = stars_encoded.drop('star_type', axis=1)
y = stars_encoded['star_type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the data to have zero mean and unit variance
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
