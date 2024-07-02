import Header from "../Header/Header";
import Main from "../Main/Main";
import Footer from "../Footer/Footer";
import Graph from "../Graph/Graph";
import "./App.scss";

const App = () => {
	return (
		<div className="container">
			<Header />
			<Main />
			<Graph />
			<Footer />
		</div>
	);
};

export default App;
