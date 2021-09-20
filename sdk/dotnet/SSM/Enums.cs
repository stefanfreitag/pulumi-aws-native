// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.SSM
{
    [EnumType]
    public readonly struct AssociationComplianceSeverity : IEquatable<AssociationComplianceSeverity>
    {
        private readonly string _value;

        private AssociationComplianceSeverity(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AssociationComplianceSeverity Critical { get; } = new AssociationComplianceSeverity("CRITICAL");
        public static AssociationComplianceSeverity High { get; } = new AssociationComplianceSeverity("HIGH");
        public static AssociationComplianceSeverity Medium { get; } = new AssociationComplianceSeverity("MEDIUM");
        public static AssociationComplianceSeverity Low { get; } = new AssociationComplianceSeverity("LOW");
        public static AssociationComplianceSeverity Unspecified { get; } = new AssociationComplianceSeverity("UNSPECIFIED");

        public static bool operator ==(AssociationComplianceSeverity left, AssociationComplianceSeverity right) => left.Equals(right);
        public static bool operator !=(AssociationComplianceSeverity left, AssociationComplianceSeverity right) => !left.Equals(right);

        public static explicit operator string(AssociationComplianceSeverity value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AssociationComplianceSeverity other && Equals(other);
        public bool Equals(AssociationComplianceSeverity other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct AssociationSyncCompliance : IEquatable<AssociationSyncCompliance>
    {
        private readonly string _value;

        private AssociationSyncCompliance(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AssociationSyncCompliance Auto { get; } = new AssociationSyncCompliance("AUTO");
        public static AssociationSyncCompliance Manual { get; } = new AssociationSyncCompliance("MANUAL");

        public static bool operator ==(AssociationSyncCompliance left, AssociationSyncCompliance right) => left.Equals(right);
        public static bool operator !=(AssociationSyncCompliance left, AssociationSyncCompliance right) => !left.Equals(right);

        public static explicit operator string(AssociationSyncCompliance value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AssociationSyncCompliance other && Equals(other);
        public bool Equals(AssociationSyncCompliance other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The key of a key-value pair that identifies the location of an attachment to a document.
    /// </summary>
    [EnumType]
    public readonly struct DocumentAttachmentsSourceKey : IEquatable<DocumentAttachmentsSourceKey>
    {
        private readonly string _value;

        private DocumentAttachmentsSourceKey(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DocumentAttachmentsSourceKey SourceUrl { get; } = new DocumentAttachmentsSourceKey("SourceUrl");
        public static DocumentAttachmentsSourceKey S3FileUrl { get; } = new DocumentAttachmentsSourceKey("S3FileUrl");
        public static DocumentAttachmentsSourceKey AttachmentReference { get; } = new DocumentAttachmentsSourceKey("AttachmentReference");

        public static bool operator ==(DocumentAttachmentsSourceKey left, DocumentAttachmentsSourceKey right) => left.Equals(right);
        public static bool operator !=(DocumentAttachmentsSourceKey left, DocumentAttachmentsSourceKey right) => !left.Equals(right);

        public static explicit operator string(DocumentAttachmentsSourceKey value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DocumentAttachmentsSourceKey other && Equals(other);
        public bool Equals(DocumentAttachmentsSourceKey other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
    /// </summary>
    [EnumType]
    public readonly struct DocumentDocumentFormat : IEquatable<DocumentDocumentFormat>
    {
        private readonly string _value;

        private DocumentDocumentFormat(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DocumentDocumentFormat Yaml { get; } = new DocumentDocumentFormat("YAML");
        public static DocumentDocumentFormat Json { get; } = new DocumentDocumentFormat("JSON");
        public static DocumentDocumentFormat Text { get; } = new DocumentDocumentFormat("TEXT");

        public static bool operator ==(DocumentDocumentFormat left, DocumentDocumentFormat right) => left.Equals(right);
        public static bool operator !=(DocumentDocumentFormat left, DocumentDocumentFormat right) => !left.Equals(right);

        public static explicit operator string(DocumentDocumentFormat value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DocumentDocumentFormat other && Equals(other);
        public bool Equals(DocumentDocumentFormat other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of document to create.
    /// </summary>
    [EnumType]
    public readonly struct DocumentDocumentType : IEquatable<DocumentDocumentType>
    {
        private readonly string _value;

        private DocumentDocumentType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DocumentDocumentType ApplicationConfiguration { get; } = new DocumentDocumentType("ApplicationConfiguration");
        public static DocumentDocumentType ApplicationConfigurationSchema { get; } = new DocumentDocumentType("ApplicationConfigurationSchema");
        public static DocumentDocumentType Automation { get; } = new DocumentDocumentType("Automation");
        public static DocumentDocumentType AutomationChangeTemplate { get; } = new DocumentDocumentType("Automation.ChangeTemplate");
        public static DocumentDocumentType ChangeCalendar { get; } = new DocumentDocumentType("ChangeCalendar");
        public static DocumentDocumentType CloudFormation { get; } = new DocumentDocumentType("CloudFormation");
        public static DocumentDocumentType Command { get; } = new DocumentDocumentType("Command");
        public static DocumentDocumentType DeploymentStrategy { get; } = new DocumentDocumentType("DeploymentStrategy");
        public static DocumentDocumentType Package { get; } = new DocumentDocumentType("Package");
        public static DocumentDocumentType Policy { get; } = new DocumentDocumentType("Policy");
        public static DocumentDocumentType ProblemAnalysis { get; } = new DocumentDocumentType("ProblemAnalysis");
        public static DocumentDocumentType ProblemAnalysisTemplate { get; } = new DocumentDocumentType("ProblemAnalysisTemplate");
        public static DocumentDocumentType Session { get; } = new DocumentDocumentType("Session");

        public static bool operator ==(DocumentDocumentType left, DocumentDocumentType right) => left.Equals(right);
        public static bool operator !=(DocumentDocumentType left, DocumentDocumentType right) => !left.Equals(right);

        public static explicit operator string(DocumentDocumentType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DocumentDocumentType other && Equals(other);
        public bool Equals(DocumentDocumentType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
