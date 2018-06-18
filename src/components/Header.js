import React, { Component } from "react";
import styled from "styled-components";
import Bg1 from "./../imgs/bg_3.svg";
import logo from "./../imgs/logo.png";
import { SearchBox, PoweredBy, Stats } from "react-instantsearch/dom";

const Container = styled.div`
  background-image: url(${Bg1});
  background-size: cover;
  background-position: center;
  z-index: 1;
  position: relative;
  width: 100%;
`;

const Wrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  align-content: initial;
  justify-content: center;
  flex-direction: column;
  padding: 75px 0;
`;

const Title = styled.h2`
  margin-bottom: 0;
`;

const SubTitle = styled.h5`
  margin-top: 0;
`;

const Img = styled.img`
  height: 5em;
`;

export const Header = () => (
  <Container>
    <Wrapper>
      <Title>
        <Img src={logo} />
      </Title>
      <SubTitle>
        Navigating between Awesome list has never been so easy!
      </SubTitle>
      <SearchBox
        translations={{
          placeholder: "Search a list by category, name, keywords ..."
        }}
      />
      <Stats
        translations={{ stats: (n, ms) => `📟  ${n} results found in ${ms}ms` }}
      />
      <PoweredBy />
    </Wrapper>
  </Container>
);
