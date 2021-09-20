// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Outputs
{

    [OutputType]
    public sealed class StudioStudioEncryptionConfiguration
    {
        public readonly string? KeyArn;
        public readonly string KeyType;

        [OutputConstructor]
        private StudioStudioEncryptionConfiguration(
            string? keyArn,

            string keyType)
        {
            KeyArn = keyArn;
            KeyType = keyType;
        }
    }
}
