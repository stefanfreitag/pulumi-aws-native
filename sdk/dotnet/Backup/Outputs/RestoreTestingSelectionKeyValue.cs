// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup.Outputs
{

    [OutputType]
    public sealed class RestoreTestingSelectionKeyValue
    {
        public readonly string Key;
        public readonly string Value;

        [OutputConstructor]
        private RestoreTestingSelectionKeyValue(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
