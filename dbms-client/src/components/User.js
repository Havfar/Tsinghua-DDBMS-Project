import React from 'react'

export default class User extends React.Component {

    constructor(props) {
    super(props)
    
    this.state = { 
        uid: undefined,
        timestamp: undefined,
        name: "Alf Prøysen",
        gender: undefined,
        email: undefined,
        phone: undefined,
        dept: undefined,
        language: undefined,
        role: undefined,
        prefer_tags: undefined,
        obtained_credits: undefined,
        showReads: false
        }
    }   

    componentDidMount(){

        const url = 'http://localhost:5000/load_user/?uid=' + this.props.uid;
        fetch(url, {
            method: 'GET',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type':'application/json'
            }
        })
        .then(response => response.json())
        .then(data => this.setState({
            uid: data.uid,
            timestamp: data.timestamp,
            name: data.name,
            gender: data.gender,
            email: data.email,
            phone: data.phone,
            dept: data.dept,
            language: data.language,
            role: data.role,
            prefer_tags: data.prefer_tags,
            obtained_credits: data.obtained_credits
        }));
    }

    toggleShowReads(){
        this.setState({showReads : !this.state.showReads})
    }

    showUserReads(){
        return (<table class="table mt-5">
            <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">First</th>
                <th scope="col">Last</th>
                <th scope="col">Handle</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
            </tr>
            </tbody>
        </table>
        )
    }
    // display the user in a div
    render () {
        return (
            <div className="card mt-3 p-2 text-left">
                <div className="row mb-4">
                    <span className="col-1"></span>
                    <div className="col-4 ">
                        <img className="img-thumbnail" src="https://nwsid.net/wp-content/uploads/2015/05/dummy-profile-pic.png"></img>
                    </div>
                    <div className="col-3"></div>
                    <div className="col-4">
                        <h3>{this.state.name}</h3>
                        <h5>{this.state.id}</h5>
                    </div>
                </div>
                <div className="row">
                    <div className="col-6">
                    <div class="form-group ">
                        <label className="mt-2" for="exampleInputEmail1">Email address</label>
                        <input value={this.state.email} disabled className="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Gender</label>
                        <input value={this.state.gender} disabled className="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Department</label>
                        <input value={this.state.email} disabled className="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Email address</label>
                        <input value={this.state.email} disabled className="form-control" />
                    </div>
                    </div>
                    <div className="col-6">
                        <label className="mt-2" for="exampleInputEmail1">Phone number</label>
                        <input value={this.state.phone} disabled class="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Language</label>
                        <input value={this.state.language} disabled class="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Role</label>
                        <input value={this.state.role} disabled class="form-control" />

                        <label className="mt-2" for="exampleInputEmail1">Prefered tags</label>
                        <input value={this.state.tags} disabled class="form-control" />
                    </div>
                </div>
                {this.showUserReads()}
            </div>
        )
    }
}