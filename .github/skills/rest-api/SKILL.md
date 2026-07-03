---
name: rest-api
description: "Use when: designing, building, testing, documenting, or debugging a REST API. Helps turn requirements into resource-oriented endpoints, request and response schemas, validation, auth, error handling, tests, and OpenAPI documentation."
---

# REST API

## Use this skill when
- You need to design or refactor a REST API
- You are implementing endpoints, payloads, or response models
- You need to add validation, authentication, pagination, or error handling
- You want to write tests, docs, or OpenAPI/Swagger definitions
- You need to debug API behavior or contract issues

## Workflow

1. Clarify the API surface
   - Identify the resources, actions, and user journeys
   - Decide on the HTTP methods, URL patterns, and status codes
   - Note auth requirements, rate limits, versioning, and pagination needs

2. Define the contract
   - Specify request and response payloads
   - Define validation rules and error responses
   - Choose consistent naming, casing, and filtering conventions
   - Document examples for success and failure cases

3. Choose an implementation approach
   - Prefer simple, maintainable layers: routes, services, models, and persistence
   - Use framework defaults for validation, serialization, and docs when available
   - Keep business logic out of handlers and expose clear interfaces

4. Implement incrementally
   - Add endpoints one resource at a time
   - Validate input early and return explicit errors
   - Keep responses consistent and predictable
   - Add logging, tracing, and observability hooks as needed

5. Verify the API
   - Write unit and integration tests for happy paths and edge cases
   - Confirm auth and permission behavior
   - Check pagination, filtering, and idempotency where applicable
   - Ensure the API is documented and examples remain accurate

6. Review for production readiness
   - Confirm status codes are correct and consistent
   - Review security, dependency, and configuration concerns
   - Verify the contract is easy to consume and evolve

## Decision points
- Use resource-oriented URLs with nouns, not verbs
- Prefer standard methods: GET, POST, PUT/PATCH, DELETE
- Return clear, consistent error payloads with appropriate status codes
- Use pagination for large collections and filtering for query-heavy endpoints
- Version the API when breaking changes are expected
- Protect sensitive operations with authentication and authorization
- Prefer explicit validation over silently accepting bad input

## Completion checklist
- Endpoint map is defined and consistent
- Request and response schemas are documented
- Validation and error handling are implemented
- Authentication and authorization are covered
- Tests exist for core flows and error cases
- API documentation or OpenAPI output is updated
- The implementation is easy to extend and maintain

## Quick starter template

Use this structure when creating a new endpoint:
- Resource path
- Allowed methods
- Request schema
- Success response schema
- Error response schema
- Auth requirements
- Example requests and responses

## Example prompts
- "Design a REST API for managing tasks with CRUD operations"
- "Add pagination and filtering to the list endpoint"
- "Implement validation and consistent error responses for this API"
- "Write tests for the auth and CRUD flows"
- "Generate OpenAPI documentation for these routes"
