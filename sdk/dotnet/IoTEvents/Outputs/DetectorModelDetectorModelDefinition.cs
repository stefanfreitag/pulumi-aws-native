// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Outputs
{

    /// <summary>
    /// Information that defines how a detector operates.
    /// </summary>
    [OutputType]
    public sealed class DetectorModelDetectorModelDefinition
    {
        /// <summary>
        /// The state that is entered at the creation of each detector (instance).
        /// </summary>
        public readonly string InitialStateName;
        /// <summary>
        /// Information about the states of the detector.
        /// </summary>
        public readonly ImmutableArray<Outputs.DetectorModelState> States;

        [OutputConstructor]
        private DetectorModelDetectorModelDefinition(
            string initialStateName,

            ImmutableArray<Outputs.DetectorModelState> states)
        {
            InitialStateName = initialStateName;
            States = states;
        }
    }
}
