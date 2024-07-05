import Header from "../Header/Header";
import Main from "../Main/Main";
import Footer from "../Footer/Footer";
import Graph from "../Graph/Graph";
import FileForm from "../FileForm/FileForm";
import "./App.scss";
import { Route, Routes } from "react-router-dom";
import ApiConnect from "../../api/ApiConnect";

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
			<ApiConnect />{" "}
			{/* arreglar, esto no es un componente, es la conexion a la apiiii */}
		</div>
	);
};

export default App;
