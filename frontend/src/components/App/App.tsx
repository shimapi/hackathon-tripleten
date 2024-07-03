import Header from "../Header/Header";
import Main from "../Main/Main";
import Footer from "../Footer/Footer";
import Graph from "../Graph/Graph";
import FileForm from "../FileForm/FileForm";
import "./App.scss";
import { Route, Routes } from "react-router-dom";

const App = () => {
	return (
		<div className="container">
			<Header />
			<Routes>
				<Route path="/" element={<Main />} />
				<Route path="/upload" element={<FileForm />} />
				<Route path="/graph" element={<Graph />} />
			</Routes>
			<Footer />
		</div>
	);
};

export default App;
