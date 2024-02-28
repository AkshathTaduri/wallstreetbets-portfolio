import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import FetchExample from './Screens/RankingsScreen';

export default function App() {
  return (
    <FetchExample />
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
