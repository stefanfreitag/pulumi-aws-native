// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// When exiting this state, perform these `actions` if the specified `condition` is `TRUE`.
    /// </summary>
    public sealed class DetectorModelOnExitArgs : global::Pulumi.ResourceArgs
    {
        [Input("events")]
        private InputList<Inputs.DetectorModelEventArgs>? _events;

        /// <summary>
        /// Specifies the `actions` that are performed when the state is exited and the `condition` is `TRUE`.
        /// </summary>
        public InputList<Inputs.DetectorModelEventArgs> Events
        {
            get => _events ?? (_events = new InputList<Inputs.DetectorModelEventArgs>());
            set => _events = value;
        }

        public DetectorModelOnExitArgs()
        {
        }
        public static new DetectorModelOnExitArgs Empty => new DetectorModelOnExitArgs();
    }
}
