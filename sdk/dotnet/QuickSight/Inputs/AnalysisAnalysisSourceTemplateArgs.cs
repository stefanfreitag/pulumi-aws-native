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
    /// &lt;p&gt;The source template of an analysis.&lt;/p&gt;
    /// </summary>
    public sealed class AnalysisAnalysisSourceTemplateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the source template of an analysis.&lt;/p&gt;
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        [Input("dataSetReferences", required: true)]
        private InputList<Inputs.AnalysisDataSetReferenceArgs>? _dataSetReferences;

        /// <summary>
        /// &lt;p&gt;The dataset references of the source template of an analysis.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.AnalysisDataSetReferenceArgs> DataSetReferences
        {
            get => _dataSetReferences ?? (_dataSetReferences = new InputList<Inputs.AnalysisDataSetReferenceArgs>());
            set => _dataSetReferences = value;
        }

        public AnalysisAnalysisSourceTemplateArgs()
        {
        }
    }
}
