// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalytics.Outputs
{

    [OutputType]
    public sealed class ApplicationReferenceDataSourceReferenceDataSource
    {
        public readonly Outputs.ApplicationReferenceDataSourceReferenceSchema ReferenceSchema;
        public readonly Outputs.ApplicationReferenceDataSourceS3ReferenceDataSource? S3ReferenceDataSource;
        public readonly string? TableName;

        [OutputConstructor]
        private ApplicationReferenceDataSourceReferenceDataSource(
            Outputs.ApplicationReferenceDataSourceReferenceSchema referenceSchema,

            Outputs.ApplicationReferenceDataSourceS3ReferenceDataSource? s3ReferenceDataSource,

            string? tableName)
        {
            ReferenceSchema = referenceSchema;
            S3ReferenceDataSource = s3ReferenceDataSource;
            TableName = tableName;
        }
    }
}
