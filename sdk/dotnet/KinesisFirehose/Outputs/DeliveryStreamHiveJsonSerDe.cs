// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Outputs
{

    [OutputType]
    public sealed class DeliveryStreamHiveJsonSerDe
    {
        public readonly ImmutableArray<string> TimestampFormats;

        [OutputConstructor]
        private DeliveryStreamHiveJsonSerDe(ImmutableArray<string> timestampFormats)
        {
            TimestampFormats = timestampFormats;
        }
    }
}
