// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFilledMapSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("categorySort")]
        private InputList<Inputs.AnalysisFieldSortOptionsArgs>? _categorySort;
        public InputList<Inputs.AnalysisFieldSortOptionsArgs> CategorySort
        {
            get => _categorySort ?? (_categorySort = new InputList<Inputs.AnalysisFieldSortOptionsArgs>());
            set => _categorySort = value;
        }

        public AnalysisFilledMapSortConfigurationArgs()
        {
        }
        public static new AnalysisFilledMapSortConfigurationArgs Empty => new AnalysisFilledMapSortConfigurationArgs();
    }
}
