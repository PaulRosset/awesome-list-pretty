import React from "react";
import styled from "styled-components";

const AuthorContainer = styled.footer`
  text-align: center;
  padding: 15px;
  line-height: 1.8;
  font-size: 14px;
`;

export const Link = styled.a`
  color: rgb(51, 53, 53);
`;

export const Authors = () => (
  <AuthorContainer>
    Made by <Link href="https://github.com/PaulRosset">Paul Rosset</Link>
    <br />
    Data Provided by the{" "}
    <Link href="https://github.com/sindresorhus/awesome/">Community</Link>
  </AuthorContainer>
);
