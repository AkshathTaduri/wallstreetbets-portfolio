import React, { useState, useEffect } from 'react';
import { FlatList, StyleSheet, Text, View } from 'react-native';

export default function App() {
  const [tickers, setTickers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await fetch("http://127.0.0.1:5050/get_rankings") // Adjust this based on your actual FetchExample implementation
        setTickers(result.tickers || []); // Extract tickers from the fetched data
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text>{item}</Text>
      {/* Add other data elements you want to display */}
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Daily Ticker Rankings</Text>
      <FlatList
        data={tickers}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()} // Use index as key if tickers don't have unique IDs
        contentContainerStyle={{ padding: 16 }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'stretch', // Adjust this based on your layout requirements
    justifyContent: 'center',
    marginTop: 40,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  item: {
    backgroundColor: '#f9f9f9',
    padding: 20,
    marginVertical: 8,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ddd',
  },
});
