# DNA to Binary Converter

## Overview

This is a web-based DNA sequence converter application built with Flask. The application provides bidirectional conversion between DNA nucleotide sequences (A, T, C, G) and binary representations (00, 11, 01, 10). Users can input either a DNA sequence or binary string, and the application will convert it to the corresponding format.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack**: HTML with embedded CSS
- **Design Pattern**: Server-side rendered templates using Jinja2
- **Styling Approach**: Inline CSS within HTML templates for simplicity
- **Rationale**: Simple single-page application doesn't require a complex frontend framework; Flask's built-in templating is sufficient for rendering forms and displaying results

### Backend Architecture

**Technology Stack**: Python Flask (lightweight web framework)
- **Request Handling**: Single route handler (`/`) supporting both GET and POST methods
- **Conversion Logic**: Two pure functions (`dna_to_binary` and `binary_to_dna`) with dictionary-based mapping
- **Error Handling**: Input validation returns error messages to the user interface
- **Rationale**: Flask provides minimal overhead for this simple conversion tool; stateless conversion functions ensure predictability and testability

**Encoding Scheme**:
- A → 00
- T → 11  
- C → 01
- G → 10
- Binary pairs are mapped back to corresponding nucleotides

**Design Decisions**:
- Dictionary-based mapping chosen for O(1) lookup performance and code readability
- Case-insensitive DNA input (converted to uppercase) for better user experience
- Binary input must be even-length (pairs of bits) with validation
- Invalid characters return None, triggering error messages

### Data Storage

**Current State**: No database or persistent storage
- All conversions are stateless and ephemeral
- Each request is processed independently without session storage
- **Rationale**: The conversion utility doesn't require data persistence; stateless architecture simplifies deployment and scaling

### Authentication & Authorization

**Current State**: No authentication implemented
- Public access to conversion functionality
- No user accounts or session management
- **Rationale**: This is a utility tool that doesn't handle sensitive data or require user-specific features

## External Dependencies

### Core Framework
- **Flask**: Python micro web framework for handling HTTP requests, routing, and template rendering

### Templating
- **Jinja2**: Built-in Flask templating engine (no separate integration needed)

### No External Services
- No third-party APIs
- No database systems
- No external authentication providers
- No cloud service integrations

The application is completely self-contained and can run independently without external dependencies beyond the Flask framework.