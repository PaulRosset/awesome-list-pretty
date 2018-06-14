import React, { Fragment } from "react";
import styled from "styled-components";
import { Hits, Highlight } from "react-instantsearch/dom";
import { Authors } from "./Authors";
import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/fontawesome-free-brands";
import { Link } from "./Authors";

const BodyContainer = styled.div`
  width: 80%;
  margin: auto;
  margin-top: 2em;
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  align-items: center;
`;

const ImgCategory = styled.img`
  height: 3em;
`;

const BodyContainerCard = styled.div`
  margin-top: 5px;
  display: flex;
  flex-direction: column;
  text-align: center;
`;

const LinkIcon = styled(Link)`
  transition: 0.3s;
  display: flex;
  align-self: center;
  &:hover {
    color: #040204;
    transition: 0.3s;
  }
`;

const Desc = styled.p`
  margin-top: 0;
`;

export const Body = () => (
  <BodyContainer>
    <Hits hitComponent={Resulting} />
    <Authors />
  </BodyContainer>
);

export const Resulting = ({ hit }) => (
  <Fragment>
    <ImgCategory src="http://via.placeholder.com/50x50" />
    <BodyContainerCard>
      <h4>{hit.name}</h4>
      <Desc>Functional programming language for the JVM.</Desc>
      <LinkIcon href={hit.url}>
        <FontAwesomeIcon icon={faGithub} size="2x" />
      </LinkIcon>
    </BodyContainerCard>
  </Fragment>
);
