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
    public sealed class StudioComponentStudioComponentInitializationScript
    {
        public readonly string? LaunchProfileProtocolVersion;
        public readonly string? Platform;
        public readonly string? RunContext;
        public readonly string? Script;

        [OutputConstructor]
        private StudioComponentStudioComponentInitializationScript(
            string? launchProfileProtocolVersion,

            string? platform,

            string? runContext,

            string? script)
        {
            LaunchProfileProtocolVersion = launchProfileProtocolVersion;
            Platform = platform;
            RunContext = runContext;
            Script = script;
        }
    }
}
