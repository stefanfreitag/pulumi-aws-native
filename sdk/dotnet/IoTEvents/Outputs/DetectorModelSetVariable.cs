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
    /// Information about the variable and its new value.
    /// </summary>
    [OutputType]
    public sealed class DetectorModelSetVariable
    {
        /// <summary>
        /// The new value of the variable.
        /// </summary>
        public readonly string Value;
        /// <summary>
        /// The name of the variable.
        /// </summary>
        public readonly string VariableName;

        [OutputConstructor]
        private DetectorModelSetVariable(
            string value,

            string variableName)
        {
            Value = value;
            VariableName = variableName;
        }
    }
}
