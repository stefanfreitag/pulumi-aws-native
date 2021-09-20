// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    [OutputType]
    public sealed class FlowS3SourceProperties
    {
        public readonly string BucketName;
        public readonly string BucketPrefix;

        [OutputConstructor]
        private FlowS3SourceProperties(
            string bucketName,

            string bucketPrefix)
        {
            BucketName = bucketName;
            BucketPrefix = bucketPrefix;
        }
    }
}
