import Header from "../Header/Header";
import Main from "../Main/Main";
import Footer from "../Footer/Footer";
import Graph from "../Graph/Graph";
import FileForm from "../FileForm/FileForm";
import "./App.scss";
import { Route, Routes } from "react-router-dom";
import ApiConnect from "../../api/ApiConnect";
import FileCsv from "../FileForm/FileCsv";

const App = () => {
	return (
		<>
			<Header />
			<div className="container">
				<Routes>
					<Route path="/" element={<Main />} />
					<Route path="/upload-json" element={<FileForm />} />
					<Route path="/upload-csv" element={<FileCsv />} />
					<Route path="/graph" element={<Graph />} />
				</Routes>
				<ApiConnect />
			</div>
			<Footer />
		</>
	);
};

export default App;
