// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Inputs
{

    public sealed class BotVersionLocaleSpecificationItemPropertiesArgs : Pulumi.ResourceArgs
    {
        [Input("botVersionLocaleDetails", required: true)]
        public Input<Inputs.BotVersionLocaleDetailsArgs> BotVersionLocaleDetails { get; set; } = null!;

        [Input("localeId", required: true)]
        public Input<string> LocaleId { get; set; } = null!;

        public BotVersionLocaleSpecificationItemPropertiesArgs()
        {
        }
    }
}
