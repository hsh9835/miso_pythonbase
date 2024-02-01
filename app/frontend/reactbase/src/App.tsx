import React, {useState} from 'react';
import axios from 'axios'
import DOMPurify from 'dompurify'

import {LineChartComponent, PieChartComponent, TreemapChartComponent} from './components/charts'

function App() {

    const [example1, setExample1] = useState("");
    const [example2, setExample2] = useState("");

    // /spacy/apple 엔드포인트에서 데이터를 가져오기 위한 비동기 함수

    const example1Data = async () => {
        axios.defaults.withCredentials = true;
        try {
            const response = await axios.post('http://127.0.0.1:8000/spacy/test');
            setExample1(response.data.message);
        } catch (error) {
            setExample1("Error occurred");
        }
    };

    const example2Data = async () => {
        axios.defaults.withCredentials = true;
        try {
            const response = await axios.post('http://127.0.0.1:8000/spacy/spaghetto');
            setExample2(response.data);
        } catch (error) {
            setExample2("Error occurred");
        }
    };


    return (
        <div className="App">
            <LineChartComponent/>
            <PieChartComponent/>
            <TreemapChartComponent/>
            <button
                style={{width: '200px', height: '50px'}}
                onClick={example1Data}
            >
                Example1
            </button>
            <EntStyle htmldata={example1}/>
            <button
                style={{width: '200px', height: '50px'}}
                onClick={example2Data}
            >
                Example2
            </button>
            <EntStyle htmldata={example2}/>
        </div>
    );
}

// 명시적으로 타입을 지정
function EntStyle({htmldata}: any) {
    const sanitizedHTML = {__html: DOMPurify.sanitize(htmldata)};
    if (htmldata) {
        return (
            <>
                <div dangerouslySetInnerHTML={sanitizedHTML}></div>
            </>
        )
    } else {
        return null
    }
}

export default App;
