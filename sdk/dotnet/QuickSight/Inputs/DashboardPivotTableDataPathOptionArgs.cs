// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardPivotTableDataPathOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataPathList", required: true)]
        private InputList<Inputs.DashboardDataPathValueArgs>? _dataPathList;
        public InputList<Inputs.DashboardDataPathValueArgs> DataPathList
        {
            get => _dataPathList ?? (_dataPathList = new InputList<Inputs.DashboardDataPathValueArgs>());
            set => _dataPathList = value;
        }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("width")]
        public Input<string>? Width { get; set; }

        public DashboardPivotTableDataPathOptionArgs()
        {
        }
        public static new DashboardPivotTableDataPathOptionArgs Empty => new DashboardPivotTableDataPathOptionArgs();
    }
}
