
import React from 'react'
import ReactDOM from 'react-dom'


export default function SearchBar(props)  {

    let alternatives = ["Hei", "hallo", "Hade"]

    return(
         <div className="md-form mt-0">
            <div className="row">
                <select class="custom-select col-2 mr-1" id="inlineFormCustomSelectPref">
                    <option selected>Choose...</option>
                    <option value="1">{alternatives[0]}</option>
                    <option value="2">{alternatives[1]}</option>
                    <option value="3">{alternatives[2]}</option>
                </select>
                <input className="form-control col" type="text" placeholder="Search" aria-label="Search"/>
            </div>
            <div className="row pt-3">
                <div class="form-group col p-0">
                    <label for="">Something</label>
                    <input className="form-control col" type="text" placeholder="Search" aria-label="Search"/>
                </div>
                <span className="col-1"/>
                <div class="form-group col p-0">
                    <label for="">Something</label>
                    <input className="form-control col" type="text" placeholder="Search" aria-label="Search"/>
                </div>
                <span className="col-1"/>
                <div class="form-group col p-0">
                    <label for="">Something</label>
                    <input className="form-control col" type="text" placeholder="Search" aria-label="Search"/>
                </div>
            </div>
            <div className="row">
                <div className="col-3">
                    <label class="my-1 mr-2 " for="inlineFormCustomSelectPref">Preference</label>
                    <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref">
                        <option selected>Choose...</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                </div>
                <div class="custom-checkbox col">
                    <input type="checkbox" class="custom-control-input" id="defaultChecked2" checked />
                    <label class="custom-control-label" for="defaultChecked2">Default checked</label>
                </div>
            </div>
            <div className="row">
                <span className="col-10"></span>
                <button type="button" class="btn btn-primary" data-toggle="button" aria-pressed="false" autocomplete="off">
                    Search
                </button>
            </div>
        </div>
    )
}

// function etSearchCategories(params) {
//     return
//         <h1></h1>

// }