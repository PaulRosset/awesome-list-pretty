import React, { Fragment } from "react";
import styled from "styled-components";
import { Hits } from "react-instantsearch/dom";
import { connectStateResults } from "react-instantsearch/connectors";
import FontAwesomeIcon from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/fontawesome-free-brands";
import { Link } from "./Authors";
import Categories from "./../categories";

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

const Category = styled.span`
  color: rgb(222, 218, 225);
  font-size: 12px;
  margin: 10px 0;
  font-weight: bold;
`;

const Awesome = styled.span`
  font-family: "Orbitron", sans-serif;
  color: #fc60a8;
`;

const Title = styled.h4`
  display: flex;
  flex-direction: column;
  margin: 10px 0;
`;

const Body = ({ searchState, searchResults }) => (
  <BodyContainer>
    {searchResults && searchResults.nbHits !== 0 ? (
      <Hits hitComponent={Resulting} />
    ) : (
      <p>No results has been found for {searchState.query}</p>
    )}
  </BodyContainer>
);

export const WrappedBody = connectStateResults(Body);

export const Resulting = ({ hit }) => (
  <Fragment>
    <ImgCategory src={Categories[hit.cat]} />
    <BodyContainerCard>
      <Title>
        <Awesome>awesome</Awesome> {hit.listName}
      </Title>
      <Category>{hit.cat}</Category>
      <Desc>{hit.desc}</Desc>
      <LinkIcon href={hit.url}>
        <FontAwesomeIcon icon={faGithub} size="2x" />
      </LinkIcon>
    </BodyContainerCard>
  </Fragment>
);
