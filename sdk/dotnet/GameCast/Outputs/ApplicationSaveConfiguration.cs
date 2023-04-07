// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameCast.Outputs
{

    /// <summary>
    /// Application save configuration
    /// </summary>
    [OutputType]
    public sealed class ApplicationSaveConfiguration
    {
        /// <summary>
        /// A list of save file, registry key or log paths that are absolute paths that store game save files when the games
        /// are running on a Windows environment.
        /// </summary>
        public readonly ImmutableArray<string> FileLocations;
        /// <summary>
        /// A list of save file, registry key or log paths that are absolute paths that store game save files when the games
        /// are running on a Windows environment.
        /// </summary>
        public readonly ImmutableArray<string> RegistryLocations;

        [OutputConstructor]
        private ApplicationSaveConfiguration(
            ImmutableArray<string> fileLocations,

            ImmutableArray<string> registryLocations)
        {
            FileLocations = fileLocations;
            RegistryLocations = registryLocations;
        }
    }
}
