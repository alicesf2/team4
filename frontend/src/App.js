import React from "react";
import logo from "./logo.svg";
import "./App.css";
import SideNav, {
  Toggle,
  Nav,
  NavItem,
  NavIcon,
  NavText
} from "@trendmicro/react-sidenav";
import "@trendmicro/react-sidenav/dist/react-sidenav.css";
import "font-awesome/css/font-awesome.min.css";

function App() {
  return (
    <SideNav
      onSelect={selected => {
        // Add your code here
      }}
    >
      <SideNav.Toggle />
      <SideNav.Nav defaultSelected="home">
        <NavItem eventKey="home">
          <NavIcon>
            <i className="fa fa-fw fa-home" style={{ fontSize: "1.75em" }} />
          </NavIcon>
          <NavText>Home</NavText>
        </NavItem>
        <NavItem eventKey="account">
          <NavIcon>
            <i className="fa fa-fw fa-user" style={{ fontSize: "1.75em" }} />
          </NavIcon>
          <NavText>Account</NavText>
          <NavItem eventKey="profile">
            <NavText>Profile</NavText>
          </NavItem>
        </NavItem>
      </SideNav.Nav>
    </SideNav>
  );
}

export default App;
