// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;List of default values defined for a given decimal dataset parameter type. Currently only static values are supported.&lt;/p&gt;
    /// </summary>
    public sealed class DataSetDecimalDatasetParameterDefaultValuesArgs : global::Pulumi.ResourceArgs
    {
        [Input("staticValues")]
        private InputList<double>? _staticValues;

        /// <summary>
        /// &lt;p&gt;List of static default values defined for a given decimal dataset parameter type.&lt;/p&gt;
        /// </summary>
        public InputList<double> StaticValues
        {
            get => _staticValues ?? (_staticValues = new InputList<double>());
            set => _staticValues = value;
        }

        public DataSetDecimalDatasetParameterDefaultValuesArgs()
        {
        }
        public static new DataSetDecimalDatasetParameterDefaultValuesArgs Empty => new DataSetDecimalDatasetParameterDefaultValuesArgs();
    }
}
