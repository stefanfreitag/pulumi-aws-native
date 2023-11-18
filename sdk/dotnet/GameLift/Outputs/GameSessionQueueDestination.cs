// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Outputs
{

    /// <summary>
    /// A fleet or alias designated in a game session queue.
    /// </summary>
    [OutputType]
    public sealed class GameSessionQueueDestination
    {
        public readonly string? DestinationArn;

        [OutputConstructor]
        private GameSessionQueueDestination(string? destinationArn)
        {
            DestinationArn = destinationArn;
        }
    }
}
