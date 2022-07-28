// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    /// <summary>
    /// Specifies default encryption for a bucket using server-side encryption with either Amazon S3-managed keys (SSE-S3) or AWS KMS-managed keys (SSE-KMS).
    /// </summary>
    public sealed class BucketEncryptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("serverSideEncryptionConfiguration", required: true)]
        private InputList<Inputs.BucketServerSideEncryptionRuleArgs>? _serverSideEncryptionConfiguration;

        /// <summary>
        /// Specifies the default server-side-encryption configuration.
        /// </summary>
        public InputList<Inputs.BucketServerSideEncryptionRuleArgs> ServerSideEncryptionConfiguration
        {
            get => _serverSideEncryptionConfiguration ?? (_serverSideEncryptionConfiguration = new InputList<Inputs.BucketServerSideEncryptionRuleArgs>());
            set => _serverSideEncryptionConfiguration = value;
        }

        public BucketEncryptionArgs()
        {
        }
        public static new BucketEncryptionArgs Empty => new BucketEncryptionArgs();
    }
}
