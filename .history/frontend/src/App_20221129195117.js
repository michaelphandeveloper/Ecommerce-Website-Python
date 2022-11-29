import Header from './components/Header'
import Footer from './components/Footer'
import { Container } from 'react-bootstrap'
import HomeScreen from "./screens/HomeScreen";

function App() {
	return (
		<div>
			<Header />
			<main>
				<Container>
					<h1>Welcome</h1>
				</Container>
			</main>
			<Footer />
		</div>
	)
}

export default App
