// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    [OutputType]
    public sealed class InstanceStorageConfigEncryptionConfig
    {
        public readonly Pulumi.AwsNative.Connect.InstanceStorageConfigEncryptionType EncryptionType;
        public readonly string KeyId;

        [OutputConstructor]
        private InstanceStorageConfigEncryptionConfig(
            Pulumi.AwsNative.Connect.InstanceStorageConfigEncryptionType encryptionType,

            string keyId)
        {
            EncryptionType = encryptionType;
            KeyId = keyId;
        }
    }
}
