// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.KinesisFirehose
{
    [EnumType]
    public readonly struct DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode : IEquatable<DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode>
    {
        private readonly string _value;

        private DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode FailedDocumentsOnly { get; } = new DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode("FailedDocumentsOnly");
        public static DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode AllDocuments { get; } = new DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode("AllDocuments");

        public static bool operator ==(DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode left, DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode left, DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode other && Equals(other);
        public bool Equals(DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationS3BackupMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod : IEquatable<DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod>
    {
        private readonly string _value;

        private DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod NoRotation { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod("NoRotation");
        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod OneHour { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod("OneHour");
        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod OneDay { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod("OneDay");
        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod OneWeek { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod("OneWeek");
        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod OneMonth { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod("OneMonth");

        public static bool operator ==(DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod left, DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod left, DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod other && Equals(other);
        public bool Equals(DeliveryStreamAmazonopensearchserviceDestinationConfigurationIndexRotationPeriod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode : IEquatable<DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode>
    {
        private readonly string _value;

        private DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode FailedDocumentsOnly { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode("FailedDocumentsOnly");
        public static DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode AllDocuments { get; } = new DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode("AllDocuments");

        public static bool operator ==(DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode left, DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode left, DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode other && Equals(other);
        public bool Equals(DeliveryStreamAmazonopensearchserviceDestinationConfigurationS3BackupMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat : IEquatable<DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat>
    {
        private readonly string _value;

        private DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat FirehoseDefault { get; } = new DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat("FIREHOSE_DEFAULT");
        public static DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat NoDocumentId { get; } = new DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat("NO_DOCUMENT_ID");

        public static bool operator ==(DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat left, DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat left, DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat other && Equals(other);
        public bool Equals(DeliveryStreamDocumentIdOptionsDefaultDocumentIdFormat other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod : IEquatable<DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod>
    {
        private readonly string _value;

        private DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod NoRotation { get; } = new DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod("NoRotation");
        public static DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod OneHour { get; } = new DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod("OneHour");
        public static DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod OneDay { get; } = new DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod("OneDay");
        public static DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod OneWeek { get; } = new DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod("OneWeek");
        public static DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod OneMonth { get; } = new DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod("OneMonth");

        public static bool operator ==(DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod left, DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod left, DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod other && Equals(other);
        public bool Equals(DeliveryStreamElasticsearchDestinationConfigurationIndexRotationPeriod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode : IEquatable<DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode>
    {
        private readonly string _value;

        private DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode FailedDocumentsOnly { get; } = new DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode("FailedDocumentsOnly");
        public static DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode AllDocuments { get; } = new DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode("AllDocuments");

        public static bool operator ==(DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode left, DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode left, DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode other && Equals(other);
        public bool Equals(DeliveryStreamElasticsearchDestinationConfigurationS3BackupMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamEncryptionConfigurationInputKeyType : IEquatable<DeliveryStreamEncryptionConfigurationInputKeyType>
    {
        private readonly string _value;

        private DeliveryStreamEncryptionConfigurationInputKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamEncryptionConfigurationInputKeyType AwsOwnedCmk { get; } = new DeliveryStreamEncryptionConfigurationInputKeyType("AWS_OWNED_CMK");
        public static DeliveryStreamEncryptionConfigurationInputKeyType CustomerManagedCmk { get; } = new DeliveryStreamEncryptionConfigurationInputKeyType("CUSTOMER_MANAGED_CMK");

        public static bool operator ==(DeliveryStreamEncryptionConfigurationInputKeyType left, DeliveryStreamEncryptionConfigurationInputKeyType right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamEncryptionConfigurationInputKeyType left, DeliveryStreamEncryptionConfigurationInputKeyType right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamEncryptionConfigurationInputKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamEncryptionConfigurationInputKeyType other && Equals(other);
        public bool Equals(DeliveryStreamEncryptionConfigurationInputKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamEncryptionConfigurationNoEncryptionConfig : IEquatable<DeliveryStreamEncryptionConfigurationNoEncryptionConfig>
    {
        private readonly string _value;

        private DeliveryStreamEncryptionConfigurationNoEncryptionConfig(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamEncryptionConfigurationNoEncryptionConfig NoEncryption { get; } = new DeliveryStreamEncryptionConfigurationNoEncryptionConfig("NoEncryption");

        public static bool operator ==(DeliveryStreamEncryptionConfigurationNoEncryptionConfig left, DeliveryStreamEncryptionConfigurationNoEncryptionConfig right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamEncryptionConfigurationNoEncryptionConfig left, DeliveryStreamEncryptionConfigurationNoEncryptionConfig right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamEncryptionConfigurationNoEncryptionConfig value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamEncryptionConfigurationNoEncryptionConfig other && Equals(other);
        public bool Equals(DeliveryStreamEncryptionConfigurationNoEncryptionConfig other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat : IEquatable<DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat>
    {
        private readonly string _value;

        private DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat Uncompressed { get; } = new DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat("UNCOMPRESSED");
        public static DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat Gzip { get; } = new DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat("GZIP");
        public static DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat Zip { get; } = new DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat("ZIP");
        public static DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat Snappy { get; } = new DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat("Snappy");
        public static DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat HadoopSnappy { get; } = new DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat("HADOOP_SNAPPY");

        public static bool operator ==(DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat left, DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat left, DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat other && Equals(other);
        public bool Equals(DeliveryStreamExtendedS3DestinationConfigurationCompressionFormat other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode : IEquatable<DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode>
    {
        private readonly string _value;

        private DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode Disabled { get; } = new DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode("Disabled");
        public static DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode Enabled { get; } = new DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode("Enabled");

        public static bool operator ==(DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode left, DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode left, DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode other && Equals(other);
        public bool Equals(DeliveryStreamExtendedS3DestinationConfigurationS3BackupMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamHttpEndpointRequestConfigurationContentEncoding : IEquatable<DeliveryStreamHttpEndpointRequestConfigurationContentEncoding>
    {
        private readonly string _value;

        private DeliveryStreamHttpEndpointRequestConfigurationContentEncoding(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamHttpEndpointRequestConfigurationContentEncoding None { get; } = new DeliveryStreamHttpEndpointRequestConfigurationContentEncoding("NONE");
        public static DeliveryStreamHttpEndpointRequestConfigurationContentEncoding Gzip { get; } = new DeliveryStreamHttpEndpointRequestConfigurationContentEncoding("GZIP");

        public static bool operator ==(DeliveryStreamHttpEndpointRequestConfigurationContentEncoding left, DeliveryStreamHttpEndpointRequestConfigurationContentEncoding right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamHttpEndpointRequestConfigurationContentEncoding left, DeliveryStreamHttpEndpointRequestConfigurationContentEncoding right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamHttpEndpointRequestConfigurationContentEncoding value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamHttpEndpointRequestConfigurationContentEncoding other && Equals(other);
        public bool Equals(DeliveryStreamHttpEndpointRequestConfigurationContentEncoding other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamProcessorType : IEquatable<DeliveryStreamProcessorType>
    {
        private readonly string _value;

        private DeliveryStreamProcessorType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamProcessorType RecordDeAggregation { get; } = new DeliveryStreamProcessorType("RecordDeAggregation");
        public static DeliveryStreamProcessorType Lambda { get; } = new DeliveryStreamProcessorType("Lambda");
        public static DeliveryStreamProcessorType MetadataExtraction { get; } = new DeliveryStreamProcessorType("MetadataExtraction");
        public static DeliveryStreamProcessorType AppendDelimiterToRecord { get; } = new DeliveryStreamProcessorType("AppendDelimiterToRecord");

        public static bool operator ==(DeliveryStreamProcessorType left, DeliveryStreamProcessorType right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamProcessorType left, DeliveryStreamProcessorType right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamProcessorType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamProcessorType other && Equals(other);
        public bool Equals(DeliveryStreamProcessorType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamRedshiftDestinationConfigurationS3BackupMode : IEquatable<DeliveryStreamRedshiftDestinationConfigurationS3BackupMode>
    {
        private readonly string _value;

        private DeliveryStreamRedshiftDestinationConfigurationS3BackupMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamRedshiftDestinationConfigurationS3BackupMode Disabled { get; } = new DeliveryStreamRedshiftDestinationConfigurationS3BackupMode("Disabled");
        public static DeliveryStreamRedshiftDestinationConfigurationS3BackupMode Enabled { get; } = new DeliveryStreamRedshiftDestinationConfigurationS3BackupMode("Enabled");

        public static bool operator ==(DeliveryStreamRedshiftDestinationConfigurationS3BackupMode left, DeliveryStreamRedshiftDestinationConfigurationS3BackupMode right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamRedshiftDestinationConfigurationS3BackupMode left, DeliveryStreamRedshiftDestinationConfigurationS3BackupMode right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamRedshiftDestinationConfigurationS3BackupMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamRedshiftDestinationConfigurationS3BackupMode other && Equals(other);
        public bool Equals(DeliveryStreamRedshiftDestinationConfigurationS3BackupMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamS3DestinationConfigurationCompressionFormat : IEquatable<DeliveryStreamS3DestinationConfigurationCompressionFormat>
    {
        private readonly string _value;

        private DeliveryStreamS3DestinationConfigurationCompressionFormat(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamS3DestinationConfigurationCompressionFormat Uncompressed { get; } = new DeliveryStreamS3DestinationConfigurationCompressionFormat("UNCOMPRESSED");
        public static DeliveryStreamS3DestinationConfigurationCompressionFormat Gzip { get; } = new DeliveryStreamS3DestinationConfigurationCompressionFormat("GZIP");
        public static DeliveryStreamS3DestinationConfigurationCompressionFormat Zip { get; } = new DeliveryStreamS3DestinationConfigurationCompressionFormat("ZIP");
        public static DeliveryStreamS3DestinationConfigurationCompressionFormat Snappy { get; } = new DeliveryStreamS3DestinationConfigurationCompressionFormat("Snappy");
        public static DeliveryStreamS3DestinationConfigurationCompressionFormat HadoopSnappy { get; } = new DeliveryStreamS3DestinationConfigurationCompressionFormat("HADOOP_SNAPPY");

        public static bool operator ==(DeliveryStreamS3DestinationConfigurationCompressionFormat left, DeliveryStreamS3DestinationConfigurationCompressionFormat right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamS3DestinationConfigurationCompressionFormat left, DeliveryStreamS3DestinationConfigurationCompressionFormat right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamS3DestinationConfigurationCompressionFormat value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamS3DestinationConfigurationCompressionFormat other && Equals(other);
        public bool Equals(DeliveryStreamS3DestinationConfigurationCompressionFormat other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamSplunkDestinationConfigurationHECEndpointType : IEquatable<DeliveryStreamSplunkDestinationConfigurationHECEndpointType>
    {
        private readonly string _value;

        private DeliveryStreamSplunkDestinationConfigurationHECEndpointType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamSplunkDestinationConfigurationHECEndpointType Raw { get; } = new DeliveryStreamSplunkDestinationConfigurationHECEndpointType("Raw");
        public static DeliveryStreamSplunkDestinationConfigurationHECEndpointType Event { get; } = new DeliveryStreamSplunkDestinationConfigurationHECEndpointType("Event");

        public static bool operator ==(DeliveryStreamSplunkDestinationConfigurationHECEndpointType left, DeliveryStreamSplunkDestinationConfigurationHECEndpointType right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamSplunkDestinationConfigurationHECEndpointType left, DeliveryStreamSplunkDestinationConfigurationHECEndpointType right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamSplunkDestinationConfigurationHECEndpointType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamSplunkDestinationConfigurationHECEndpointType other && Equals(other);
        public bool Equals(DeliveryStreamSplunkDestinationConfigurationHECEndpointType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DeliveryStreamType : IEquatable<DeliveryStreamType>
    {
        private readonly string _value;

        private DeliveryStreamType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DeliveryStreamType DirectPut { get; } = new DeliveryStreamType("DirectPut");
        public static DeliveryStreamType KinesisStreamAsSource { get; } = new DeliveryStreamType("KinesisStreamAsSource");

        public static bool operator ==(DeliveryStreamType left, DeliveryStreamType right) => left.Equals(right);
        public static bool operator !=(DeliveryStreamType left, DeliveryStreamType right) => !left.Equals(right);

        public static explicit operator string(DeliveryStreamType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DeliveryStreamType other && Equals(other);
        public bool Equals(DeliveryStreamType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
