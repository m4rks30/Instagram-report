import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('instagram_data.csv')

data = data.dropna(how='all')
data = data.drop_duplicates()
data['engagement_rate'] = (data['likes'] + data['comments']) / data['followers']
threshold = np.mean(data['engagement_rate']) + 2 * np.std(data['engagement_rate'])
spam_accounts = data[data['engagement_rate'] > threshold]['username'].tolist()
top_performing_accounts = data.nlargest(5, 'engagement_rate')['username'].tolist()
hashtags = data['hashtags'].str.split(',', expand=True).stack().str.strip().value_counts().nlargest(5).index.tolist()
print(f"Total number of posts: {len(data)}")
print(f"Total number of followers: {data['followers'].sum()}")
print(f"Average engagement rate: {data['engagement_rate'].mean()}")
print(f"Potential spam accounts: {', '.join(spam_accounts)}")
print(f"Top performing accounts: {', '.join(top_performing_accounts)}")
print(f"Top hashtags: {', '.join(hashtags)}")
plt.hist(data['engagement_rate'], bins=20)
plt.axvline(threshold, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('Engagement Rate')
plt.ylabel('Frequency')
plt.title('Distribution of Engagement Rates')
plt.show()
